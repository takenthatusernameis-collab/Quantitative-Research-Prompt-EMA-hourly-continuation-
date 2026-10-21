# EMA Hourly Continuation — NFT/USDT P12_144

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.4233 |
| net_win_rate | 0.3570 |
| gross_profit_factor | 0.6545 |
| gross_win_rate | 0.3593 |
| sharpe_ratio | -6.5758 |
| sortino_ratio | -1.9710 |
| max_drawdown | 0.9066 |
| cagr | -0.6051 |
| net_avg_win | 42.4875 |
| net_avg_loss | -55.7236 |
| avg_hold_time_bars | 28.3455 |
| exposure | 0.5630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
