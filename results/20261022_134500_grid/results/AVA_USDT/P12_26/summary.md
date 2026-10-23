# EMA Hourly Continuation — AVA/USDT P12_26

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1308 |
| net_profit_factor | 0.2823 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.6865 |
| gross_win_rate | 0.4320 |
| sharpe_ratio | -11.7019 |
| sortino_ratio | -6.0092 |
| max_drawdown | 0.9995 |
| cagr | -0.9529 |
| net_avg_win | 7.4032 |
| net_avg_loss | -17.9234 |
| avg_hold_time_bars | 3.0910 |
| exposure | 0.1838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
