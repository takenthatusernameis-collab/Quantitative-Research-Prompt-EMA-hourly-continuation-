# EMA Hourly Continuation — AVA/USDT P12_89

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.5472 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.8851 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -4.6038 |
| sortino_ratio | -1.7855 |
| max_drawdown | 0.8959 |
| cagr | -0.5854 |
| net_avg_win | 29.0854 |
| net_avg_loss | -48.5578 |
| avg_hold_time_bars | 13.6477 |
| exposure | 0.4808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
