# EMA Hourly Continuation — NFT/USDT P21_89

**Symbol:** NFT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1250 |
| net_profit_factor | 0.2821 |
| net_win_rate | 0.2384 |
| gross_profit_factor | 0.7028 |
| gross_win_rate | 0.2808 |
| sharpe_ratio | -19.5866 |
| sortino_ratio | -10.5690 |
| max_drawdown | 1.0000 |
| cagr | -0.9970 |
| net_avg_win | 13.1850 |
| net_avg_loss | -14.6314 |
| avg_hold_time_bars | 6.9232 |
| exposure | 0.3934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
