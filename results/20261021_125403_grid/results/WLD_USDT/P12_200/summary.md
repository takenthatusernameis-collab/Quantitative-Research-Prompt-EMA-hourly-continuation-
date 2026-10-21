# EMA Hourly Continuation — WLD/USDT P12_200

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.9961 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1042 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | 0.0303 |
| sortino_ratio | 0.0070 |
| max_drawdown | 0.1624 |
| cagr | -0.0020 |
| net_avg_win | 96.7030 |
| net_avg_loss | -108.3150 |
| avg_hold_time_bars | 65.1562 |
| exposure | 0.7582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
