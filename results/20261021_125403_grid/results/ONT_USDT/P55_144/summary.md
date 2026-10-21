# EMA Hourly Continuation — ONT/USDT P55_144

**Symbol:** ONT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.6559 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.1662 |
| sortino_ratio | -0.5597 |
| max_drawdown | 0.5011 |
| cagr | -0.2274 |
| net_avg_win | 58.8255 |
| net_avg_loss | -78.9901 |
| avg_hold_time_bars | 16.9909 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
