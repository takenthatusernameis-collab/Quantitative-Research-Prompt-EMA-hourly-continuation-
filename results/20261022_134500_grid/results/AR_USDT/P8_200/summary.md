# EMA Hourly Continuation — AR/USDT P8_200

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.8616 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0520 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -0.6920 |
| sortino_ratio | -0.1502 |
| max_drawdown | 0.2331 |
| cagr | -0.0687 |
| net_avg_win | 86.3980 |
| net_avg_loss | -105.6496 |
| avg_hold_time_bars | 83.0913 |
| exposure | 0.8687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
