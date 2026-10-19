# EMA Hourly Continuation — NFT/USDT P12_21

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 2052 |
| net_profit_factor | 0.0881 |
| net_win_rate | 0.1486 |
| gross_profit_factor | 0.4981 |
| gross_win_rate | 0.2373 |
| sharpe_ratio | -31.2646 |
| sortino_ratio | -23.5899 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 3.1675 |
| net_avg_loss | -6.2771 |
| avg_hold_time_bars | 2.1711 |
| exposure | 0.2025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
