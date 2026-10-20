# EMA Hourly Continuation — REZ/USDT P20_144

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.8720 |
| net_win_rate | 0.5304 |
| gross_profit_factor | 1.1268 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -0.9465 |
| sortino_ratio | -0.2915 |
| max_drawdown | 0.3804 |
| cagr | -0.1317 |
| net_avg_win | 82.3170 |
| net_avg_loss | -106.6409 |
| avg_hold_time_bars | 26.1587 |
| exposure | 0.5552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
