# EMA Hourly Continuation — MOG/USDT P50_55

**Symbol:** MOG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 85 |
| net_profit_factor | 0.7676 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -0.8150 |
| sortino_ratio | -0.1124 |
| max_drawdown | 0.1733 |
| cagr | -0.0506 |
| net_avg_win | 88.4348 |
| net_avg_loss | -112.5230 |
| avg_hold_time_bars | 5.7647 |
| exposure | 0.0244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
