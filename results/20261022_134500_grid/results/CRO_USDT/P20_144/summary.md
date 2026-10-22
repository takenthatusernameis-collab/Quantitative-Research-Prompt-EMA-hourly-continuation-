# EMA Hourly Continuation — CRO/USDT P20_144

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.5825 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 1.0258 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -3.6735 |
| sortino_ratio | -1.1173 |
| max_drawdown | 0.7652 |
| cagr | -0.4256 |
| net_avg_win | 45.5977 |
| net_avg_loss | -72.8866 |
| avg_hold_time_bars | 26.8574 |
| exposure | 0.5823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
