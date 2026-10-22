# EMA Hourly Continuation — TAO/USDT P34_55

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.5383 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.9270 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -6.9586 |
| sortino_ratio | -2.8819 |
| max_drawdown | 0.9733 |
| cagr | -0.7615 |
| net_avg_win | 28.7830 |
| net_avg_loss | -44.3522 |
| avg_hold_time_bars | 3.0276 |
| exposure | 0.1196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
