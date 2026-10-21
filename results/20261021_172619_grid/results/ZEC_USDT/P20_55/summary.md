# EMA Hourly Continuation — ZEC/USDT P20_55

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.8751 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0993 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.8907 |
| sortino_ratio | -0.2691 |
| max_drawdown | 0.3217 |
| cagr | -0.1195 |
| net_avg_win | 83.3119 |
| net_avg_loss | -104.2684 |
| avg_hold_time_bars | 9.3977 |
| exposure | 0.1880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
