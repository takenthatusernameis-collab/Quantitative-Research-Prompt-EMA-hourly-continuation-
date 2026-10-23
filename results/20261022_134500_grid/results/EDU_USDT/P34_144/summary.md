# EMA Hourly Continuation — EDU/USDT P34_144

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.6446 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -3.1723 |
| sortino_ratio | -1.0236 |
| max_drawdown | 0.7139 |
| cagr | -0.3828 |
| net_avg_win | 52.1077 |
| net_avg_loss | -71.2432 |
| avg_hold_time_bars | 18.2275 |
| exposure | 0.4314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
