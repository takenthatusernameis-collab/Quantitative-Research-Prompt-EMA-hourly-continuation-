# EMA Hourly Continuation — TAO/USDT P50_55

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 771 |
| net_profit_factor | 0.2767 |
| net_win_rate | 0.3684 |
| gross_profit_factor | 0.6601 |
| gross_win_rate | 0.4008 |
| sharpe_ratio | -11.1084 |
| sortino_ratio | -4.4579 |
| max_drawdown | 0.9978 |
| cagr | -0.9124 |
| net_avg_win | 13.4424 |
| net_avg_loss | -28.3276 |
| avg_hold_time_bars | 1.8975 |
| exposure | 0.0665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
