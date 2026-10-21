# EMA Hourly Continuation — GTC/USDT P8_144

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.7473 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8913 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -1.9000 |
| sortino_ratio | -0.5580 |
| max_drawdown | 0.5001 |
| cagr | -0.2266 |
| net_avg_win | 69.9709 |
| net_avg_loss | -83.2708 |
| avg_hold_time_bars | 35.2670 |
| exposure | 0.6845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
