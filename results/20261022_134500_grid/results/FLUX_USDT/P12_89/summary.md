# EMA Hourly Continuation — FLUX/USDT P12_89

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -3.6206 |
| sortino_ratio | -1.3905 |
| max_drawdown | 0.8195 |
| cagr | -0.4891 |
| net_avg_win | 39.5746 |
| net_avg_loss | -58.6841 |
| avg_hold_time_bars | 15.3960 |
| exposure | 0.5249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
