# EMA Hourly Continuation — SNX/USDT P50_144

**Symbol:** SNX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6887 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 1.0754 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -2.8332 |
| sortino_ratio | -0.8662 |
| max_drawdown | 0.6532 |
| cagr | -0.3387 |
| net_avg_win | 61.7661 |
| net_avg_loss | -86.6952 |
| avg_hold_time_bars | 13.6737 |
| exposure | 0.2920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
