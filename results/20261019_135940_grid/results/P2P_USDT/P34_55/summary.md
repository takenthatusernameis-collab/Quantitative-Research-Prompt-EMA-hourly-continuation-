# EMA Hourly Continuation — P2P/USDT P34_55

**Symbol:** P2P/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.3280 |
| net_win_rate | 0.3383 |
| gross_profit_factor | 0.5822 |
| gross_win_rate | 0.3408 |
| sharpe_ratio | -9.3864 |
| sortino_ratio | -3.7535 |
| max_drawdown | 0.9909 |
| cagr | -0.8461 |
| net_avg_win | 17.7182 |
| net_avg_loss | -27.6144 |
| avg_hold_time_bars | 4.1846 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
