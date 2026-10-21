# EMA Hourly Continuation — BDX/USDT P50_55

**Symbol:** BDX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 113 |
| net_profit_factor | 0.2144 |
| net_win_rate | 0.2566 |
| gross_profit_factor | 0.3610 |
| gross_win_rate | 0.2566 |
| sharpe_ratio | -4.6259 |
| sortino_ratio | -0.7168 |
| max_drawdown | 0.5731 |
| cagr | -0.2875 |
| net_avg_win | 53.9356 |
| net_avg_loss | -86.8487 |
| avg_hold_time_bars | 4.4513 |
| exposure | 0.0229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
