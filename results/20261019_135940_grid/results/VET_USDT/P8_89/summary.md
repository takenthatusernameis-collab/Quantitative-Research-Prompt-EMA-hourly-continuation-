# EMA Hourly Continuation — VET/USDT P8_89

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.1403 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -3.2038 |
| sortino_ratio | -1.2147 |
| max_drawdown | 0.7835 |
| cagr | -0.4429 |
| net_avg_win | 55.3204 |
| net_avg_loss | -79.6566 |
| avg_hold_time_bars | 18.9821 |
| exposure | 0.6273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
