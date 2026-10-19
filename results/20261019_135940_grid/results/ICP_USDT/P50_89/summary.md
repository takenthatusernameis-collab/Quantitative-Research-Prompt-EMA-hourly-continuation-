# EMA Hourly Continuation — ICP/USDT P50_89

**Symbol:** ICP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.4541 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.8401 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -6.0175 |
| sortino_ratio | -2.2533 |
| max_drawdown | 0.9407 |
| cagr | -0.6721 |
| net_avg_win | 23.6065 |
| net_avg_loss | -45.3973 |
| avg_hold_time_bars | 4.4507 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
