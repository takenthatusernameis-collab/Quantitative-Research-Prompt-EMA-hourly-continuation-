# EMA Hourly Continuation — MEW/USDT P8_20

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7524 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -2.6178 |
| sortino_ratio | -0.9034 |
| max_drawdown | 0.7020 |
| cagr | -0.3402 |
| net_avg_win | 69.0757 |
| net_avg_loss | -88.4011 |
| avg_hold_time_bars | 5.3373 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
