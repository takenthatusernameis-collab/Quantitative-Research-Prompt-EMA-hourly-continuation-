# EMA Hourly Continuation — NFT/USDT P12_34

**Symbol:** NFT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1853 |
| net_profit_factor | 0.1547 |
| net_win_rate | 0.2035 |
| gross_profit_factor | 0.5615 |
| gross_win_rate | 0.2747 |
| sharpe_ratio | -26.5162 |
| sortino_ratio | -18.0104 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 4.8528 |
| net_avg_loss | -8.0146 |
| avg_hold_time_bars | 3.3308 |
| exposure | 0.2805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
