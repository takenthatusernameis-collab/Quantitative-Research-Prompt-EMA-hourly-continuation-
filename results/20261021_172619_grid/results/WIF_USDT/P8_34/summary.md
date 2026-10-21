# EMA Hourly Continuation — WIF/USDT P8_34

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.9318 |
| net_win_rate | 0.5305 |
| gross_profit_factor | 1.1243 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -0.5769 |
| sortino_ratio | -0.2133 |
| max_drawdown | 0.4246 |
| cagr | -0.1011 |
| net_avg_win | 92.1526 |
| net_avg_loss | -111.7437 |
| avg_hold_time_bars | 8.9085 |
| exposure | 0.2656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
