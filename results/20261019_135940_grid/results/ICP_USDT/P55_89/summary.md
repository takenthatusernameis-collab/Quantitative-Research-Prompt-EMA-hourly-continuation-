# EMA Hourly Continuation — ICP/USDT P55_89

**Symbol:** ICP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4482 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -6.1978 |
| sortino_ratio | -2.3233 |
| max_drawdown | 0.9447 |
| cagr | -0.6809 |
| net_avg_win | 23.4286 |
| net_avg_loss | -45.4612 |
| avg_hold_time_bars | 3.7411 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
