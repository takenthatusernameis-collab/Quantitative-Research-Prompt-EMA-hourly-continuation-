# EMA Hourly Continuation — ARPA/USDT P50_144

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.4621 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.7235 |
| gross_win_rate | 0.4309 |
| sharpe_ratio | -5.5569 |
| sortino_ratio | -1.8546 |
| max_drawdown | 0.8966 |
| cagr | -0.5916 |
| net_avg_win | 32.4635 |
| net_avg_loss | -50.9154 |
| avg_hold_time_bars | 11.5745 |
| exposure | 0.2954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
