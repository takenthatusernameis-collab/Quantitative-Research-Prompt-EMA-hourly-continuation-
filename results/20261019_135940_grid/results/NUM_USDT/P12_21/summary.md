# EMA Hourly Continuation — NUM/USDT P12_21

**Symbol:** NUM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.2566 |
| net_win_rate | 0.3158 |
| gross_profit_factor | 0.6721 |
| gross_win_rate | 0.3451 |
| sharpe_ratio | -15.7338 |
| sortino_ratio | -8.2713 |
| max_drawdown | 1.0000 |
| cagr | -0.9867 |
| net_avg_win | 8.2199 |
| net_avg_loss | -14.7826 |
| avg_hold_time_bars | 3.2143 |
| exposure | 0.1943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
