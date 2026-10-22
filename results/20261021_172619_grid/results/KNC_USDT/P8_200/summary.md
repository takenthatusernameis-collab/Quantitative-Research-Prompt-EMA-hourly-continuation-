# EMA Hourly Continuation — KNC/USDT P8_200

**Symbol:** KNC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.8959 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -1.4999 |
| sortino_ratio | -0.3373 |
| max_drawdown | 0.3551 |
| cagr | -0.1437 |
| net_avg_win | 72.2071 |
| net_avg_loss | -88.9891 |
| avg_hold_time_bars | 74.1080 |
| exposure | 0.8421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
