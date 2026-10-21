# EMA Hourly Continuation — APT/USDT P20_34

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8154 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -2.5216 |
| sortino_ratio | -0.6077 |
| max_drawdown | 0.5287 |
| cagr | -0.2429 |
| net_avg_win | 56.1466 |
| net_avg_loss | -80.4147 |
| avg_hold_time_bars | 5.9193 |
| exposure | 0.0767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
