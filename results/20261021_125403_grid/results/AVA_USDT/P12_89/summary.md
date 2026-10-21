# EMA Hourly Continuation — AVA/USDT P12_89

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.8724 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0796 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.8827 |
| sortino_ratio | -0.2941 |
| max_drawdown | 0.4008 |
| cagr | -0.1301 |
| net_avg_win | 72.1440 |
| net_avg_loss | -90.8013 |
| avg_hold_time_bars | 18.9664 |
| exposure | 0.4612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
