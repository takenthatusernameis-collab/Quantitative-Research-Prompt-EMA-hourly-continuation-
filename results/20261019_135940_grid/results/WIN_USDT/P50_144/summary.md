# EMA Hourly Continuation — WIN/USDT P50_144

**Symbol:** WIN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.3847 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.7232 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -6.0190 |
| sortino_ratio | -1.8301 |
| max_drawdown | 0.9005 |
| cagr | -0.6010 |
| net_avg_win | 30.1060 |
| net_avg_loss | -52.8315 |
| avg_hold_time_bars | 13.2608 |
| exposure | 0.2797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
