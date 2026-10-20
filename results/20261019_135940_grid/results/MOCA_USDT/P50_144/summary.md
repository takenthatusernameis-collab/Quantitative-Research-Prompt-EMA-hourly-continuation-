# EMA Hourly Continuation — MOCA/USDT P50_144

**Symbol:** MOCA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5341 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.8002 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -4.4851 |
| sortino_ratio | -1.3738 |
| max_drawdown | 0.7880 |
| cagr | -0.4919 |
| net_avg_win | 46.9378 |
| net_avg_loss | -69.1470 |
| avg_hold_time_bars | 12.5688 |
| exposure | 0.2747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
