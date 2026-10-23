# EMA Hourly Continuation — ALT/USDT P21_89

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.6419 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9083 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -3.4907 |
| sortino_ratio | -1.2776 |
| max_drawdown | 0.7880 |
| cagr | -0.4509 |
| net_avg_win | 44.1286 |
| net_avg_loss | -61.5453 |
| avg_hold_time_bars | 12.2317 |
| exposure | 0.3720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
