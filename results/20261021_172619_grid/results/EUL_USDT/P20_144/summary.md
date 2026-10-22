# EMA Hourly Continuation — EUL/USDT P20_144

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8133 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.1414 |
| sortino_ratio | -0.3061 |
| max_drawdown | 0.3404 |
| cagr | -0.1327 |
| net_avg_win | 75.2543 |
| net_avg_loss | -89.9489 |
| avg_hold_time_bars | 31.9887 |
| exposure | 0.5133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
