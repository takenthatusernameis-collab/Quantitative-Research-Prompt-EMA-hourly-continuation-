# EMA Hourly Continuation — WIF/USDT P12_26

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.9083 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1409 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.6296 |
| sortino_ratio | -0.1749 |
| max_drawdown | 0.3687 |
| cagr | -0.0806 |
| net_avg_win | 95.7513 |
| net_avg_loss | -120.0367 |
| avg_hold_time_bars | 5.2432 |
| exposure | 0.0882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
