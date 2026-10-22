# EMA Hourly Continuation — APE/USDT P55_144

**Symbol:** APE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6190 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9774 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -2.8794 |
| sortino_ratio | -0.9276 |
| max_drawdown | 0.6654 |
| cagr | -0.3534 |
| net_avg_win | 42.0684 |
| net_avg_loss | -67.6964 |
| avg_hold_time_bars | 11.3301 |
| exposure | 0.2652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
