# EMA Hourly Continuation — ETH/USDT P20_55

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6711 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.6772 |
| sortino_ratio | -0.8041 |
| max_drawdown | 0.6169 |
| cagr | -0.3064 |
| net_avg_win | 56.2643 |
| net_avg_loss | -83.8354 |
| avg_hold_time_bars | 9.5596 |
| exposure | 0.1895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
