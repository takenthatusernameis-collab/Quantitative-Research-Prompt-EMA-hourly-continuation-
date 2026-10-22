# EMA Hourly Continuation — PEOPLE/USDT P55_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7288 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.8866 |
| sortino_ratio | -0.5214 |
| max_drawdown | 0.4876 |
| cagr | -0.2124 |
| net_avg_win | 66.0896 |
| net_avg_loss | -87.8154 |
| avg_hold_time_bars | 6.9786 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
