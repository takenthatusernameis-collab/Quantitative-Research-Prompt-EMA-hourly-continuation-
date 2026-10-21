# EMA Hourly Continuation — STX/USDT P12_100

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.7581 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -1.7139 |
| sortino_ratio | -0.5075 |
| max_drawdown | 0.5210 |
| cagr | -0.2092 |
| net_avg_win | 66.6733 |
| net_avg_loss | -82.4505 |
| avg_hold_time_bars | 30.8940 |
| exposure | 0.6067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
