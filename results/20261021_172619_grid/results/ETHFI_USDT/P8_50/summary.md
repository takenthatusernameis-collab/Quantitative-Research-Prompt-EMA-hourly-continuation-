# EMA Hourly Continuation — ETHFI/USDT P8_50

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.7741 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.0206 |
| sortino_ratio | -0.7396 |
| max_drawdown | 0.5911 |
| cagr | -0.2898 |
| net_avg_win | 62.1508 |
| net_avg_loss | -74.8680 |
| avg_hold_time_bars | 14.4962 |
| exposure | 0.4342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
