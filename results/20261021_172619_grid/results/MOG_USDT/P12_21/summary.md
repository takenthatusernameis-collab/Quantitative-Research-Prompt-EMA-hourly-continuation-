# EMA Hourly Continuation — MOG/USDT P12_21

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8156 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -2.6807 |
| sortino_ratio | -0.6881 |
| max_drawdown | 0.5240 |
| cagr | -0.2721 |
| net_avg_win | 70.8268 |
| net_avg_loss | -87.9398 |
| avg_hold_time_bars | 5.6221 |
| exposure | 0.0836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
