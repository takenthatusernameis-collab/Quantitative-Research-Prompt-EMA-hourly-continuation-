# EMA Hourly Continuation — BCH/USDT P12_55

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -2.2673 |
| sortino_ratio | -0.7755 |
| max_drawdown | 0.5901 |
| cagr | -0.2989 |
| net_avg_win | 58.2548 |
| net_avg_loss | -80.7856 |
| avg_hold_time_bars | 12.5238 |
| exposure | 0.3228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
