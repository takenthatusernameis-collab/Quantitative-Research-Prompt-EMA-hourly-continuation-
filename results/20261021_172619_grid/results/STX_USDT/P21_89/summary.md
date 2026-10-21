# EMA Hourly Continuation — STX/USDT P21_89

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7535 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -1.8742 |
| sortino_ratio | -0.5840 |
| max_drawdown | 0.5215 |
| cagr | -0.2359 |
| net_avg_win | 64.3688 |
| net_avg_loss | -81.9265 |
| avg_hold_time_bars | 16.5439 |
| exposure | 0.3578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
