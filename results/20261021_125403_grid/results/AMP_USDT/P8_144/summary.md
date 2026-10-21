# EMA Hourly Continuation — AMP/USDT P8_144

**Symbol:** AMP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5050 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.6313 |
| gross_win_rate | 0.4048 |
| sharpe_ratio | -4.4449 |
| sortino_ratio | -1.4572 |
| max_drawdown | 0.8278 |
| cagr | -0.4912 |
| net_avg_win | 38.0529 |
| net_avg_loss | -51.2447 |
| avg_hold_time_bars | 26.2015 |
| exposure | 0.6443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
