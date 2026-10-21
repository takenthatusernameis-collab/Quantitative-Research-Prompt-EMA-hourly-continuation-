# EMA Hourly Continuation — RSR/USDT P34_89

**Symbol:** RSR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.8203 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0216 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.3641 |
| sortino_ratio | -0.4051 |
| max_drawdown | 0.4315 |
| cagr | -0.1714 |
| net_avg_win | 79.4975 |
| net_avg_loss | -98.2830 |
| avg_hold_time_bars | 11.5245 |
| exposure | 0.2247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
