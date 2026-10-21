# EMA Hourly Continuation — MOVR/USDT P26_34

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8591 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -2.6169 |
| sortino_ratio | -0.5965 |
| max_drawdown | 0.5329 |
| cagr | -0.2398 |
| net_avg_win | 62.0507 |
| net_avg_loss | -89.3174 |
| avg_hold_time_bars | 4.5945 |
| exposure | 0.0530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
