# EMA Hourly Continuation — BSV/USDT P8_12

**Symbol:** BSV/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6444 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9896 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.4291 |
| sortino_ratio | -0.6065 |
| max_drawdown | 0.5205 |
| cagr | -0.2416 |
| net_avg_win | 60.8709 |
| net_avg_loss | -92.6037 |
| avg_hold_time_bars | 5.2226 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
