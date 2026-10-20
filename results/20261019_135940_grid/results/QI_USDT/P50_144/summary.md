# EMA Hourly Continuation — QI/USDT P50_144

**Symbol:** QI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.4720 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7570 |
| gross_win_rate | 0.4338 |
| sharpe_ratio | -4.9788 |
| sortino_ratio | -1.5479 |
| max_drawdown | 0.8531 |
| cagr | -0.5249 |
| net_avg_win | 36.9423 |
| net_avg_loss | -56.0965 |
| avg_hold_time_bars | 12.3707 |
| exposure | 0.2749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
