# EMA Hourly Continuation — STX/USDT P55_200

**Symbol:** STX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6378 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.3912 |
| sortino_ratio | -0.6264 |
| max_drawdown | 0.5327 |
| cagr | -0.2574 |
| net_avg_win | 54.3814 |
| net_avg_loss | -81.4489 |
| avg_hold_time_bars | 24.2914 |
| exposure | 0.3847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
