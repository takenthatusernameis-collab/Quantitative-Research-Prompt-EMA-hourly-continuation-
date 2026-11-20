# EMA Hourly Continuation — P2P/USDT P12_200

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6586 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8042 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -2.4419 |
| sortino_ratio | -0.6550 |
| max_drawdown | 0.5650 |
| cagr | -0.2630 |
| net_avg_win | 64.5254 |
| net_avg_loss | -77.9926 |
| avg_hold_time_bars | 44.3546 |
| exposure | 0.7278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
