# EMA Hourly Continuation — ENS/USDT P8_55

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.5546 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -6.4072 |
| sortino_ratio | -2.9462 |
| max_drawdown | 0.9732 |
| cagr | -0.7603 |
| net_avg_win | 24.4565 |
| net_avg_loss | -37.7014 |
| avg_hold_time_bars | 10.3706 |
| exposure | 0.5063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
