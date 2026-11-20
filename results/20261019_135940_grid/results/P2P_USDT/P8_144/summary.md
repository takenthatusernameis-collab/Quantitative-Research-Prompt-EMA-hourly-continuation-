# EMA Hourly Continuation — P2P/USDT P8_144

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.8034 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -3.3069 |
| sortino_ratio | -1.0366 |
| max_drawdown | 0.7138 |
| cagr | -0.3905 |
| net_avg_win | 56.4625 |
| net_avg_loss | -69.2840 |
| avg_hold_time_bars | 31.9960 |
| exposure | 0.7301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
