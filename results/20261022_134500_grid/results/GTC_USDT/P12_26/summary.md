# EMA Hourly Continuation — GTC/USDT P12_26

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1231 |
| net_profit_factor | 0.4273 |
| net_win_rate | 0.4192 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -9.7314 |
| sortino_ratio | -4.8371 |
| max_drawdown | 0.9975 |
| cagr | -0.9077 |
| net_avg_win | 14.4227 |
| net_avg_loss | -24.3593 |
| avg_hold_time_bars | 3.6702 |
| exposure | 0.2054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
