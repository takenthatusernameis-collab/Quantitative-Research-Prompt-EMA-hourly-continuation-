# EMA Hourly Continuation — MANA/USDT P12_89

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5457 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.8899 |
| gross_win_rate | 0.4314 |
| sharpe_ratio | -6.4447 |
| sortino_ratio | -2.3031 |
| max_drawdown | 0.9515 |
| cagr | -0.6934 |
| net_avg_win | 40.9895 |
| net_avg_loss | -54.2373 |
| avg_hold_time_bars | 19.1388 |
| exposure | 0.5768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
